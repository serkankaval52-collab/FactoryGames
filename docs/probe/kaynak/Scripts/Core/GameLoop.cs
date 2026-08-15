using System;
using System.Collections.Generic;

namespace FactoryProbe.Core
{
    public enum GameState
    {
        Running,
        Failed,
        Completed
    }

    /// <summary>
    /// Cekirdek dongu — Unity API'si YOK. EditMode testi bunu dogrudan surer,
    /// PlayMode botu ayni sinifi gercek oyun katmani uzerinden surer (tek kaynak).
    /// </summary>
    public sealed class GameLoop
    {
        private readonly GameConfig _cfg;
        private readonly List<Gate> _gates = new List<Gate>(32);

        private float _elapsed;
        private int _spawnedGates;

        public GameState State { get; private set; }
        public float PlayerY { get; private set; }
        public int PassedGates { get; private set; }
        public int Score { get; private set; }
        public float Elapsed => _elapsed;
        public IReadOnlyList<Gate> Gates => _gates;

        /// <summary>Skor degistiginde tetiklenir (kural 14: UnityEvent degil, C# event).</summary>
        public event Action<int> ScoreChanged;

        /// <summary>Durum degistiginde tetiklenir.</summary>
        public event Action<GameState> StateChanged;

        public GameLoop(GameConfig cfg)
        {
            _cfg = cfg ?? throw new ArgumentNullException(nameof(cfg));
            _cfg.Validate();
            Restart();
        }

        public void Restart()
        {
            _gates.Clear();
            _elapsed = 0f;
            _spawnedGates = 0;
            PlayerY = 0f;
            PassedGates = 0;
            Score = 0;
            SetState(GameState.Running);
            ScoreChanged?.Invoke(Score);
        }

        public void Tick(float dt, bool holding)
        {
            if (dt <= 0f) throw new ArgumentOutOfRangeException(nameof(dt), "dt pozitif olmali");
            if (State != GameState.Running) return;

            _elapsed += dt;
            MovePlayer(dt, holding);

            if (GateRules.OutOfBounds(PlayerY, _cfg.playerHalfSize, _cfg.worldHalfHeight))
            {
                Fail();
                return;
            }

            SpawnDueGates();
            if (AdvanceGates(dt)) return; // carpisma oldu

            if (_spawnedGates >= _cfg.gateCount && _gates.Count == 0)
            {
                Score = ScoreRules.Total(PassedGates, _cfg.pointsPerGate, true, _cfg.completionBonus);
                ScoreChanged?.Invoke(Score);
                SetState(GameState.Completed);
            }
        }

        private void MovePlayer(float dt, bool holding)
        {
            float speed = holding ? _cfg.riseSpeed : -_cfg.fallSpeed;
            PlayerY += speed * dt;
        }

        private void SpawnDueGates()
        {
            while (_spawnedGates < _cfg.gateCount &&
                   _elapsed >= _cfg.startDelaySeconds + _spawnedGates * _cfg.gateIntervalSeconds)
            {
                _gates.Add(new Gate
                {
                    Index = _spawnedGates,
                    X = _cfg.gateSpawnX,
                    GapCenter = GateRules.GapCenter(_spawnedGates, _cfg.gapAmplitude, _cfg.gapPhaseStep),
                    Scored = false
                });
                _spawnedGates++;
            }
        }

        /// <summary>Kapilari ilerletir; carpisma olduysa true doner.</summary>
        private bool AdvanceGates(float dt)
        {
            for (int i = _gates.Count - 1; i >= 0; i--)
            {
                Gate g = _gates[i];
                g.X -= _cfg.gateSpeed * dt;

                if (GateRules.Hits(g, _cfg.playerX, PlayerY, _cfg.playerHalfSize,
                                   _cfg.gateHalfWidth, _cfg.gateGapHalf))
                {
                    _gates[i] = g;
                    Fail();
                    return true;
                }

                if (!g.Scored && GateRules.PassedPlayer(g, _cfg.playerX, _cfg.gateHalfWidth))
                {
                    g.Scored = true;
                    PassedGates++;
                    Score = ScoreRules.Total(PassedGates, _cfg.pointsPerGate, false, _cfg.completionBonus);
                    ScoreChanged?.Invoke(Score);
                }

                if (g.X < _cfg.playerX - 4f)
                {
                    _gates.RemoveAt(i);
                    continue;
                }

                _gates[i] = g;
            }
            return false;
        }

        private void Fail()
        {
            Score = ScoreRules.Total(PassedGates, _cfg.pointsPerGate, false, _cfg.completionBonus);
            ScoreChanged?.Invoke(Score);
            SetState(GameState.Failed);
        }

        private void SetState(GameState next)
        {
            if (State == next) return;
            State = next;
            StateChanged?.Invoke(next);
        }
    }
}
