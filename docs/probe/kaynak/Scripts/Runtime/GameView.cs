using System.Collections.Generic;
using FactoryProbe.Core;
using UnityEngine;

namespace FactoryProbe.Runtime
{
    /// <summary>
    /// Uygulayici katman: cizim + girdi aktarimi. IS KURALI ICERMEZ (kod-standardi §1) —
    /// tum karar GameLoop'ta. Sahne dosyasina dokunmaz; her sey runtime'da kurulur.
    /// </summary>
    public sealed class GameView : MonoBehaviour
    {
        private const int GATE_POOL = 10;   // ayni anda ekranda olabilecek kapi ust siniri
        private const float GATE_WALL_LENGTH = 12f;

        private GameConfig _cfg;
        private GameLoop _loop;
        private IInputSource _input;

        private Transform _player;
        private readonly List<Transform> _topWalls = new List<Transform>(GATE_POOL);
        private readonly List<Transform> _bottomWalls = new List<Transform>(GATE_POOL);

        private string _scoreText = "0";     // Update'te string allokasyonu yok (kural 16):
        private string _stateText = "";      // yalnizca degistiginde yeniden uretilir
        private string _configSource = "";

        public GameLoop Loop => _loop;
        public GameConfig Config => _cfg;
        public string ConfigSource => _configSource;

        /// <summary>Bot/test girdi kaynagini degistirir (scripted input).</summary>
        public void SetInputSource(IInputSource source)
        {
            _input = source;
        }

        internal void Initialize(GameConfig cfg, string configSource, IInputSource input)
        {
            _cfg = cfg;
            _configSource = configSource;
            _input = input;

            _loop = new GameLoop(cfg);
            _loop.ScoreChanged += OnScoreChanged;
            _loop.StateChanged += OnStateChanged;

            BuildVisuals();
            OnScoreChanged(_loop.Score);
            OnStateChanged(_loop.State);
        }

        private void OnDestroy()
        {
            if (_loop != null)
            {
                _loop.ScoreChanged -= OnScoreChanged;
                _loop.StateChanged -= OnStateChanged;
            }
            if (GameRoot.View == this) GameRoot.Clear();
        }

        private void OnScoreChanged(int score) => _scoreText = score.ToString();

        private void OnStateChanged(GameState state)
        {
            switch (state)
            {
                case GameState.Failed: _stateText = "CARPTI — dokun ve yeniden basla"; break;
                case GameState.Completed: _stateText = "TUR TAMAM — dokun ve yeniden basla"; break;
                default: _stateText = ""; break;
            }
        }

        private void Update()
        {
            if (_loop == null) return;

            _input.Sample();

            if (_loop.State != GameState.Running)
            {
                // Fail/tamamlanma sonrasi TEK dokunusla restart (brief gereksinimi).
                if (_input.PressedThisFrame) _loop.Restart();
            }
            else
            {
                _loop.Tick(Time.deltaTime, _input.IsHolding);
            }

            SyncVisuals();
        }

        private void BuildVisuals()
        {
            Sprite unit = SpriteFactory.UnitSquare();

            _player = SpriteFactory.Spawn(transform, "Player", unit, new Color(0.20f, 0.85f, 0.95f), 10);
            _player.localScale = new Vector3(_cfg.playerHalfSize * 2f, _cfg.playerHalfSize * 2f, 1f);

            Color wallColor = new Color(0.95f, 0.45f, 0.30f);
            for (int i = 0; i < GATE_POOL; i++)
            {
                Transform top = SpriteFactory.Spawn(transform, "GateTop", unit, wallColor, 5);
                Transform bottom = SpriteFactory.Spawn(transform, "GateBottom", unit, wallColor, 5);
                top.localScale = new Vector3(_cfg.gateHalfWidth * 2f, GATE_WALL_LENGTH, 1f);
                bottom.localScale = top.localScale;
                top.gameObject.SetActive(false);
                bottom.gameObject.SetActive(false);
                _topWalls.Add(top);
                _bottomWalls.Add(bottom);
            }
        }

        private void SyncVisuals()
        {
            _player.localPosition = new Vector3(_cfg.playerX, _loop.PlayerY, 0f);

            IReadOnlyList<Gate> gates = _loop.Gates;
            int shown = gates.Count < GATE_POOL ? gates.Count : GATE_POOL;

            for (int i = 0; i < shown; i++)
            {
                Gate g = gates[i];
                float half = GATE_WALL_LENGTH * 0.5f;

                Transform top = _topWalls[i];
                Transform bottom = _bottomWalls[i];
                if (!top.gameObject.activeSelf) top.gameObject.SetActive(true);
                if (!bottom.gameObject.activeSelf) bottom.gameObject.SetActive(true);

                top.localPosition = new Vector3(g.X, g.GapCenter + _cfg.gateGapHalf + half, 0f);
                bottom.localPosition = new Vector3(g.X, g.GapCenter - _cfg.gateGapHalf - half, 0f);
            }

            for (int i = shown; i < GATE_POOL; i++)
            {
                if (_topWalls[i].gameObject.activeSelf) _topWalls[i].gameObject.SetActive(false);
                if (_bottomWalls[i].gameObject.activeSelf) _bottomWalls[i].gameObject.SetActive(false);
            }
        }

        private void OnGUI()
        {
            // HUD icin TextMeshPro kullanilmadi: font asset'i ScriptableObject'tir
            // ve kural 9 (.asset yok) ile celisir. IMGUI asset gerektirmez.
            GUI.Label(new Rect(16f, 12f, 300f, 28f), "SKOR: " + _scoreText);
            if (_stateText.Length > 0)
                GUI.Label(new Rect(16f, 40f, 460f, 28f), _stateText);
        }
    }
}
