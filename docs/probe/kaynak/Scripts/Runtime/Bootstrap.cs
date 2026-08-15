using FactoryProbe.Core;
using UnityEngine;

namespace FactoryProbe.Runtime
{
    /// <summary>
    /// Tum sahne kurulumu buradan, saf C#'tan yapilir (Sozlesme-2):
    /// sahne dosyasi sablon varsayilani olarak KALIR, hicbir nesne elle eklenmez.
    /// </summary>
    public static class Bootstrap
    {
        public const string ROOT_NAME = "FactoryProbeRoot";

        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
        public static void Boot()
        {
            if (GameRoot.View != null) return; // idempotent: iki kez kurulmaz

            GameConfig cfg = ConfigLoader.Load(out string source);

            GameObject root = new GameObject(ROOT_NAME);
            Object.DontDestroyOnLoad(root);

            CreateCamera(root.transform, cfg);

            GameView view = root.AddComponent<GameView>();
            view.Initialize(cfg, source, new UnityInputSource());
            GameRoot.Register(view);

#if UNITY_EDITOR || DEVELOPMENT_BUILD
            Debug.Log($"[FactoryProbe] boot ok — config: {source}; beklenen tur: {cfg.ExpectedRunSeconds():F1} sn");
#endif
        }

        /// <summary>
        /// Kendi kameramizi kurariz: sahnedeki Main Camera'ya `Camera.main` /
        /// `FindFirstObjectByType` ile ULASILMAZ (kural 8) ve sahne dosyasi degismez.
        /// </summary>
        private static void CreateCamera(Transform parent, GameConfig cfg)
        {
            GameObject camGo = new GameObject("ProbeCamera");
            camGo.transform.SetParent(parent, false);
            camGo.transform.localPosition = new Vector3(0f, 0f, -10f);

            Camera cam = camGo.AddComponent<Camera>();
            cam.orthographic = true;
            cam.orthographicSize = cfg.worldHalfHeight;
            cam.clearFlags = CameraClearFlags.SolidColor;
            cam.backgroundColor = new Color(0.08f, 0.10f, 0.14f);
            cam.depth = 10f;   // sahnenin sablon kamerasinin ustune cizer
            cam.nearClipPlane = 0.1f;
            cam.farClipPlane = 50f;
        }
    }
}
