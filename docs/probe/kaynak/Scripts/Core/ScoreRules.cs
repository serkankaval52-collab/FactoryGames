namespace FactoryProbe.Core
{
    /// <summary>Skor formulunun tek kaynagi (kod-standardi §1: formul kopyalanmaz).</summary>
    public static class ScoreRules
    {
        public static int ForGates(int passedGates, int pointsPerGate)
        {
            return passedGates * pointsPerGate;
        }

        public static int Total(int passedGates, int pointsPerGate, bool completed, int completionBonus)
        {
            int score = ForGates(passedGates, pointsPerGate);
            return completed ? score + completionBonus : score;
        }
    }
}
