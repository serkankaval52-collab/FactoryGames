using System.Collections.Generic;

namespace FactoryProbe.Core
{
    /// <summary>
    /// Deterministik bot pilotu — saf. "Scripted input" budur: gercek girdi
    /// katmani yerine bu sinif hold/release uretir, ayni cekirdek dongu kosar.
    /// </summary>
    public static class BotPilot
    {
        /// <summary>Hedef yukseklik: onundeki ilk kapinin bosluk merkezi; kapi yoksa merkez.</summary>
        public static float TargetY(IReadOnlyList<Gate> gates, float playerX, float gateHalfWidth)
        {
            float best = 0f;
            float bestX = float.MaxValue;
            for (int i = 0; i < gates.Count; i++)
            {
                Gate g = gates[i];
                if (GateRules.PassedPlayer(g, playerX, gateHalfWidth)) continue;
                if (g.X < bestX)
                {
                    bestX = g.X;
                    best = g.GapCenter;
                }
            }
            return best;
        }

        /// <summary>Basit esikli kontrol: hedefin altindaysa tut, ustundeyse birak.</summary>
        public static bool ShouldHold(float playerY, float targetY, float deadZone = 0.05f)
        {
            return playerY < targetY - deadZone;
        }
    }
}
