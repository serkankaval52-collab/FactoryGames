using UnityEngine;

namespace FactoryProbe.Runtime
{
    /// <summary>
    /// Gercek girdi: fare (editor/masaustu) veya dokunma (mobil).
    /// Legacy Input Manager kullanilir — preset revizyonu 1 ile
    /// activeInputHandler = 0 (bkz. presets/unity-6000.3.16f1/README.md).
    /// </summary>
    public sealed class UnityInputSource : IInputSource
    {
        private bool _holding;
        private bool _wasHolding;

        public bool IsHolding => _holding;
        public bool PressedThisFrame => _holding && !_wasHolding;

        public void Sample()
        {
            _wasHolding = _holding;

            bool touch = Input.touchCount > 0 &&
                         Input.GetTouch(0).phase != TouchPhase.Ended &&
                         Input.GetTouch(0).phase != TouchPhase.Canceled;

            _holding = touch || Input.GetMouseButton(0);
        }
    }
}
