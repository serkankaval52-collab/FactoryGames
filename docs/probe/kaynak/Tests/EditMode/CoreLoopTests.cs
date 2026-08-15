using System.IO;
using FactoryProbe.Core;
using NUnit.Framework;
using UnityEngine;

namespace FactoryProbe.Tests.EditMode
{
    /// <summary>
    /// Cekirdek mantik testleri — Unity sahnesi YOK, saf sinif surulur.
    /// Deterministik sabit zaman adimi kullanilir (kirilgan test olcumu kirletir).
    /// </summary>
    public sealed class CoreLoopTests
    {
        private const float DT = 1f / 60f;

        private static GameConfig Cfg() => new GameConfig();

        [Test]
        public void Config_Defaults_AreValid()
        {
            Assert.DoesNotThrow(() => Cfg().Validate());
        }

        [Test]
        public void Config_RunLength_IsWithinBriefBand_60_90()
        {
            float seconds = Cfg().ExpectedRunSeconds();
            Assert.GreaterOrEqual(seconds, 60f, "tur 60 sn'den kisa");
            Assert.LessOrEqual(seconds, 90f, "tur 90 sn'den uzun");
        }

        [Test]
        public void StreamingAssets_Config_MatchesDefaults()
        {
            string path = Path.Combine(Application.streamingAssetsPath, ConfigLoaderFileName);
            Assert.IsTrue(File.Exists(path), "StreamingAssets config dosyasi yok: " + path);

            GameConfig fromJson = JsonUtility.FromJson<GameConfig>(File.ReadAllText(path));
            Assert.IsNotNull(fromJson, "config JSON cozumlenemedi");
            Assert.DoesNotThrow(() => fromJson.Validate());

            GameConfig defaults = Cfg();
            Assert.AreEqual(defaults.gateCount, fromJson.gateCount, "gateCount JSON ile kod varsayilani ayrildi");
            Assert.AreEqual(defaults.pointsPerGate, fromJson.pointsPerGate, "pointsPerGate ayrildi");
        }

        private const string ConfigLoaderFileName = "game-config.json";

        [Test]
        public void Score_Formula_IsSingleSource()
        {
            Assert.AreEqual(30, ScoreRules.ForGates(3, 10));
            Assert.AreEqual(80, ScoreRules.Total(3, 10, true, 50));
            Assert.AreEqual(30, ScoreRules.Total(3, 10, false, 50));
        }

        [Test]
        public void Gap_Placement_IsDeterministic()
        {
            float a = GateRules.GapCenter(7, 2.6f, 0.9f);
            float b = GateRules.GapCenter(7, 2.6f, 0.9f);
            Assert.AreEqual(a, b, 0f, "ayni indeks farkli sonuc verdi — rastgelelik sizmis");
        }

        [Test]
        public void Player_FallsOutOfWorld_WithoutInput_AndFails()
        {
            GameLoop loop = new GameLoop(Cfg());
            for (int i = 0; i < 60 * 10 && loop.State == GameState.Running; i++)
                loop.Tick(DT, false);

            Assert.AreEqual(GameState.Failed, loop.State, "girdi olmadan oyuncu dusup fail etmeliydi");
        }

        [Test]
        public void Hold_RaisesPlayer()
        {
            GameLoop loop = new GameLoop(Cfg());
            float start = loop.PlayerY;
            for (int i = 0; i < 30; i++) loop.Tick(DT, true);

            Assert.Greater(loop.PlayerY, start, "basili tutmak oyuncuyu yukseltmedi");
        }

        [Test]
        public void Restart_ResetsScoreAndState()
        {
            GameLoop loop = new GameLoop(Cfg());
            for (int i = 0; i < 60 * 10 && loop.State == GameState.Running; i++)
                loop.Tick(DT, false);
            Assert.AreEqual(GameState.Failed, loop.State);

            loop.Restart();
            Assert.AreEqual(GameState.Running, loop.State);
            Assert.AreEqual(0, loop.Score);
            Assert.AreEqual(0, loop.PassedGates);
            Assert.AreEqual(0f, loop.PlayerY, 0.0001f);
        }

        [Test]
        public void Collision_Detected_WhenOutsideGap()
        {
            Gate g = new Gate { Index = 0, X = -6.0f, GapCenter = 3.0f, Scored = false };
            bool hit = GateRules.Hits(g, -6.0f, 0.0f, 0.35f, 0.35f, 1.15f);
            Assert.IsTrue(hit, "bosluk disindaki oyuncu carpismaliydi");

            bool clear = GateRules.Hits(g, -6.0f, 3.0f, 0.35f, 0.35f, 1.15f);
            Assert.IsFalse(clear, "bosluk merkezindeki oyuncu carpismamaliydi");
        }

        [Test]
        public void BotPilot_CompletesFullRun_Deterministically()
        {
            GameConfig cfg = Cfg();
            GameLoop loop = new GameLoop(cfg);

            int guard = (int)((cfg.ExpectedRunSeconds() + 10f) * 60f);
            for (int i = 0; i < guard && loop.State == GameState.Running; i++)
            {
                float target = BotPilot.TargetY(loop.Gates, cfg.playerX, cfg.gateHalfWidth);
                loop.Tick(DT, BotPilot.ShouldHold(loop.PlayerY, target));
            }

            Assert.AreEqual(GameState.Completed, loop.State,
                $"bot turu tamamlayamadi (durum={loop.State}, gecilen={loop.PassedGates})");
            Assert.AreEqual(cfg.gateCount, loop.PassedGates, "tum kapilar gecilmedi");
        }
    }
}
