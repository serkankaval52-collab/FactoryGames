using System;

namespace FactoryProbe.Core
{
    /// <summary>Tek bir kapinin durumu (saf veri).</summary>
    public struct Gate
    {
        public int Index;
        public float X;
        public float GapCenter;
        public bool Scored;
    }

    /// <summary>
    /// Kapi yerlesimi ve carpisma kurallari — tek kaynak.
    /// Formul kopyalanmaz: hem oyun hem bot hem test buradan cagirir (Sozlesme-2).
    /// </summary>
    public static class GateRules
    {
        /// <summary>Kapi bosluk merkezi: deterministik, rastgelelik yok.</summary>
        public static float GapCenter(int index, float amplitude, float phaseStep)
        {
            return amplitude * (float)Math.Sin(index * phaseStep);
        }

        /// <summary>Oyuncu bu kapiyla carpisiyor mu? (eksen-hizali kutu testi)</summary>
        public static bool Hits(in Gate gate, float playerX, float playerY,
                                float playerHalfSize, float gateHalfWidth, float gapHalf)
        {
            bool xOverlap = Math.Abs(gate.X - playerX) <= (gateHalfWidth + playerHalfSize);
            if (!xOverlap) return false;

            bool insideGap = Math.Abs(playerY - gate.GapCenter) + playerHalfSize <= gapHalf;
            return !insideGap;
        }

        /// <summary>Kapi oyuncunun x'ini gecti mi? (skor tetigi)</summary>
        public static bool PassedPlayer(in Gate gate, float playerX, float gateHalfWidth)
        {
            return gate.X + gateHalfWidth < playerX;
        }

        /// <summary>Oyuncu dunya disina cikti mi? (fail tetigi)</summary>
        public static bool OutOfBounds(float playerY, float playerHalfSize, float worldHalfHeight)
        {
            return Math.Abs(playerY) + playerHalfSize > worldHalfHeight;
        }
    }
}
