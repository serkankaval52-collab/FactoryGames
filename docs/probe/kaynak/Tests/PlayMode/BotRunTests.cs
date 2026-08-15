using System.Collections;
using System.IO;
using System.Text;
using FactoryProbe.Core;
using FactoryProbe.Runtime;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

namespace FactoryProbe.Tests.PlayMode
{
    /// <summary>
    /// Bot ile 3 otomatik dongu — gercek oyun katmani uzerinden (scripted input).
    /// Zaman adimi SABIT (Time.captureDeltaTime): kirilgan test olcumu kirletir.
    /// </summary>
    public sealed class BotRunTests
    {
        private const float STEP = 1f / 60f;
        private const int LOOPS = 3;

        /// <summary>Girdi katmanina takilan bot: gercek dokunus yerine bunu kullanir.</summary>
        private sealed class BotInputSource : IInputSource
        {
            private readonly GameView _view;
            private bool _holding;
            private bool _wasHolding;

            public BotInputSource(GameView view) => _view = view;

            public bool IsHolding => _holding;
            public bool PressedThisFrame => _holding && !_wasHolding;

            public void Sample()
            {
                _wasHolding = _holding;
                GameLoop loop = _view.Loop;
                GameConfig cfg = _view.Config;

                if (loop.State != GameState.Running)
                {
                    // Fail/tamamlanma ekraninda tek dokunus: bir kare bas, sonra birak.
                    _holding = !_wasHolding;
                    return;
                }

                float target = BotPilot.TargetY(loop.Gates, cfg.playerX, cfg.gateHalfWidth);
                _holding = BotPilot.ShouldHold(loop.PlayerY, target);
            }
        }

        private int _logCount;

        [SetUp]
        public void SetUp()
        {
            _logCount = 0;
            Application.logMessageReceived += OnLog;
        }

        [TearDown]
        public void TearDown()
        {
            Application.logMessageReceived -= OnLog;
            Time.captureDeltaTime = 0f;
        }

        private void OnLog(string condition, string stackTrace, LogType type)
        {
            if (type == LogType.Error || type == LogType.Exception || type == LogType.Assert)
                _logCount++;
        }

        [UnityTest]
        public IEnumerator Bot_Runs_Three_Loops_Without_Errors()
        {
            Assert.IsNotNull(GameRoot.View,
                "Bootstrap calismadi: GameRoot.View bos (RuntimeInitializeOnLoadMethod bekleniyordu)");

            GameView view = GameRoot.View;
            GameConfig cfg = view.Config;
            BotInputSource bot = new BotInputSource(view);
            view.SetInputSource(bot);
            view.Loop.Restart();

            Time.captureDeltaTime = STEP;   // deterministik zaman adimi

            StringBuilder log = new StringBuilder();
            log.AppendLine("# FactoryProbe bot kosusu");
            log.AppendLine($"config kaynagi : {view.ConfigSource}");
            log.AppendLine($"beklenen tur   : {cfg.ExpectedRunSeconds():F2} sn");
            log.AppendLine($"zaman adimi    : {STEP:F5} sn (captureDeltaTime)");
            log.AppendLine($"dongu sayisi   : {LOOPS}");
            log.AppendLine();

            int guardFrames = Mathf.CeilToInt((cfg.ExpectedRunSeconds() + 15f) / STEP);

            for (int loopIndex = 1; loopIndex <= LOOPS; loopIndex++)
            {
                int frames = 0;
                while (view.Loop.State == GameState.Running && frames < guardFrames)
                {
                    yield return null;
                    frames++;
                }

                GameState state = view.Loop.State;
                float simSeconds = frames * STEP;
                log.AppendLine($"dongu {loopIndex}: durum={state} gecilen_kapi={view.Loop.PassedGates} " +
                               $"skor={view.Loop.Score} kare={frames} sim_sure={simSeconds:F2} sn");

                Assert.AreEqual(GameState.Completed, state,
                    $"dongu {loopIndex} tamamlanamadi (durum={state}, gecilen={view.Loop.PassedGates})");
                Assert.AreEqual(cfg.gateCount, view.Loop.PassedGates, $"dongu {loopIndex}: kapi sayisi tutmadi");
                Assert.GreaterOrEqual(simSeconds, 60f, $"dongu {loopIndex}: tur 60 sn altinda");
                Assert.LessOrEqual(simSeconds, 90f, $"dongu {loopIndex}: tur 90 sn ustunde");

                // Fail/tamamlanma ekraninda TEK dokunusla restart (brief gereksinimi).
                yield return null;   // bot bir kare basar
                yield return null;   // birakir
                Assert.AreEqual(GameState.Running, view.Loop.State,
                    $"dongu {loopIndex} sonrasi tek dokunusla restart olmadi");
            }

            log.AppendLine();
            log.AppendLine($"hata/exception log sayisi: {_logCount}");
            WriteLog(log.ToString());

            Assert.AreEqual(0, _logCount, "kosuda hata/exception logu uretildi");
        }

        private static void WriteLog(string content)
        {
            string dir = Path.Combine(Application.dataPath, "..", "Logs");
            Directory.CreateDirectory(dir);
            File.WriteAllText(Path.Combine(dir, "bot-run.log"), content);
        }
    }
}
