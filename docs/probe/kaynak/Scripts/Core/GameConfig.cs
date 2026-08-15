using System;

namespace FactoryProbe.Core
{
    /// <summary>
    /// Ayarlanabilir tüm degerlerin tek kaynagi (StreamingAssets/game-config.json).
    /// Saf veri: Unity API'sine dokunmaz, EditMode testi bunu dogrudan kurar.
    /// </summary>
    [Serializable]
    public sealed class GameConfig
    {
        // Oyuncu dikey hareketi (birim/saniye)
        public float riseSpeed = 3.2f;
        public float fallSpeed = 3.6f;

        // Dunya sinirlari (kamera yariyuksekligiyle uyumlu)
        public float worldHalfHeight = 4.5f;
        public float playerX = -6.0f;
        public float playerHalfSize = 0.35f;

        // Kapi akisi
        public float gateSpeed = 4.0f;
        public float gateSpawnX = 10.0f;
        public float gateIntervalSeconds = 3.0f;
        public int gateCount = 24;
        public float startDelaySeconds = 3.0f;
        public float gateGapHalf = 1.15f;
        public float gateHalfWidth = 0.35f;

        // Bosluk merkezi deterministik formulle uretilir (rastgelelik YOK:
        // bot tekrarlanabilir olmali, kirilgan test olcumu kirletir).
        public float gapAmplitude = 2.6f;
        public float gapPhaseStep = 0.9f;

        // Skor
        public int pointsPerGate = 10;
        public int completionBonus = 50;

        /// <summary>Turun teorik suresi (sn) — brief'in 60-90 sn bandi bu degerle olculur.</summary>
        public float ExpectedRunSeconds()
        {
            // Son kapinin uretiminden sonra oyuncuya ulasmasi da sure alir.
            float lastSpawn = startDelaySeconds + (gateCount - 1) * gateIntervalSeconds;
            float travel = (gateSpawnX - playerX) / gateSpeed;
            return lastSpawn + travel;
        }

        public void Validate()
        {
            if (riseSpeed <= 0f || fallSpeed <= 0f) throw new ArgumentException("hiz degerleri pozitif olmali");
            if (gateSpeed <= 0f) throw new ArgumentException("gateSpeed pozitif olmali");
            if (gateCount <= 0) throw new ArgumentException("gateCount pozitif olmali");
            if (gateIntervalSeconds <= 0f) throw new ArgumentException("gateIntervalSeconds pozitif olmali");
            if (worldHalfHeight <= 0f) throw new ArgumentException("worldHalfHeight pozitif olmali");
            if (gateGapHalf <= playerHalfSize) throw new ArgumentException("bosluk oyuncudan genis olmali");
            if (gapAmplitude + gateGapHalf > worldHalfHeight)
                throw new ArgumentException("bosluk merkezi dunya disina tasiyor");
        }
    }
}
