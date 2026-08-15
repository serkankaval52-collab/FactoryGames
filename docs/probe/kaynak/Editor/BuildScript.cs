using System;
using System.IO;
using UnityEditor;
using UnityEditor.Build;
using UnityEditor.Build.Reporting;
using UnityEngine;

namespace FactoryProbe.EditorTools
{
    /// <summary>
    /// Yerel Android build — derlenebilirlik kanitidir (brief: "APK uretimi CI disi,
    /// yerel build yeterli"). Sahne listesi BURADA acikca verilir; EditorBuildSettings
    /// varliğina bagimli degildir (kaynagi olmayan durum yaratmamak icin).
    /// </summary>
    public static class BuildScript
    {
        private const string SCENE = "Assets/Scenes/SampleScene.unity";

        // Sablonun productName'i "2D_URP" — RAKAMLA baslar; Unity'nin urettigi
        // varsayilan kimlik "com.DefaultCompany.2D_URP" Android'de gecersizdir
        // (her segment harfle baslamali) ve build "Package Name has not been set up
        // correctly" ile duser. Kimlik burada, KODDA verilir: kaynagi olan durum.
        private const string APPLICATION_ID = "com.factorygames.probe";

        public static void BuildAndroid()
        {
            PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.Android, APPLICATION_ID);

            string outDir = Path.Combine(Directory.GetCurrentDirectory(), "Build");
            Directory.CreateDirectory(outDir);
            string apk = Path.Combine(outDir, "probe.apk");

            if (!File.Exists(SCENE))
                throw new FileNotFoundException("sahne bulunamadi: " + SCENE);

            BuildPlayerOptions opts = new BuildPlayerOptions
            {
                scenes = new[] { SCENE },
                locationPathName = apk,
                target = BuildTarget.Android,
                targetGroup = BuildTargetGroup.Android,
                options = BuildOptions.None
            };

            BuildReport report = BuildPipeline.BuildPlayer(opts);
            BuildSummary s = report.summary;

            Debug.Log($"[FactoryProbe] build sonucu={s.result} sure={s.totalTime} " +
                      $"boyut={s.totalSize} hata={s.totalErrors} uyari={s.totalWarnings} cikti={s.outputPath}");

            if (s.result != BuildResult.Succeeded)
                throw new Exception($"Android build basarisiz: {s.result}, hata={s.totalErrors}");
        }
    }
}
