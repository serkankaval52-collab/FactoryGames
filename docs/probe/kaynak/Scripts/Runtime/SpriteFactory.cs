using UnityEngine;

namespace FactoryProbe.Runtime
{
    /// <summary>
    /// Gorseller kod tarafindan uretilir: repoda ham görüntü artefakti yok (kural 25)
    /// ve .asset uretmez (kural 9). Tek 1x1 doku paylasilir, olcek Transform'dan gelir.
    /// </summary>
    public static class SpriteFactory
    {
        private static Sprite _unitSquare;

        public static Sprite UnitSquare()
        {
            if (_unitSquare != null) return _unitSquare;

            Texture2D tex = new Texture2D(1, 1, TextureFormat.RGBA32, false)
            {
                name = "FactoryProbe_Unit",
                filterMode = FilterMode.Point,
                wrapMode = TextureWrapMode.Clamp,
                hideFlags = HideFlags.HideAndDontSave
            };
            tex.SetPixel(0, 0, Color.white);
            tex.Apply();

            _unitSquare = Sprite.Create(tex, new Rect(0f, 0f, 1f, 1f), new Vector2(0.5f, 0.5f), 1f);
            _unitSquare.name = "FactoryProbe_UnitSquare";
            _unitSquare.hideFlags = HideFlags.HideAndDontSave;
            return _unitSquare;
        }

        public static Transform Spawn(Transform parent, string name, Sprite sprite, Color color, int order)
        {
            GameObject go = new GameObject(name);
            go.transform.SetParent(parent, false);
            SpriteRenderer sr = go.AddComponent<SpriteRenderer>();
            sr.sprite = sprite;
            sr.color = color;
            sr.sortingOrder = order;
            return go.transform;
        }
    }
}
