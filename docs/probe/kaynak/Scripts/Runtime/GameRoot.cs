namespace FactoryProbe.Runtime
{
    /// <summary>
    /// Kurulum aninda ACIK atama ile doldurulan tek erisim noktasi.
    /// `GameObject.Find` / `FindFirstObjectByType` kullanilmaz (kural 8):
    /// Bootstrap nesneyi yaratirken referansi buraya yazar.
    /// </summary>
    public static class GameRoot
    {
        public static GameView View { get; private set; }

        public static void Register(GameView view)
        {
            View = view;
        }

        public static void Clear()
        {
            View = null;
        }
    }
}
