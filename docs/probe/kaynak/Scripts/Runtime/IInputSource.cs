namespace FactoryProbe.Runtime
{
    /// <summary>
    /// Girdi yuzeyi tek arayuzun arkasinda: gercek dokunus ile bot girdisi
    /// ayni dongude kosar (kod-standardi §5 — acik baglama, Find yok).
    /// </summary>
    public interface IInputSource
    {
        /// <summary>Bu karede ekrana basili tutuluyor mu?</summary>
        bool IsHolding { get; }

        /// <summary>Bu karede basma YENI baslamis mi? (fail sonrasi restart tetigi)</summary>
        bool PressedThisFrame { get; }

        void Sample();
    }
}
