using System;
using System.IO;
using FactoryProbe.Core;
using UnityEngine;

namespace FactoryProbe.Runtime
{
    /// <summary>
    /// Ayarlarin tek kaynagi: StreamingAssets/game-config.json.
    /// Okunamazsa SESSIZ varsayim yapilmaz (kural 6) — durum acikca raporlanir.
    /// </summary>
    public static class ConfigLoader
    {
        public const string FILE_NAME = "game-config.json";

        public static GameConfig Load(out string source)
        {
            string path = Path.Combine(Application.streamingAssetsPath, FILE_NAME);
            try
            {
                if (File.Exists(path))
                {
                    string json = File.ReadAllText(path);
                    GameConfig cfg = JsonUtility.FromJson<GameConfig>(json);
                    if (cfg != null)
                    {
                        cfg.Validate();
                        source = path;
                        return cfg;
                    }
                    throw new InvalidDataException("JSON cozumlendi ama nesne bos dondu");
                }
                source = "VARSAYILAN (dosya yok: " + path + ")";
            }
            catch (Exception ex)
            {
                source = "VARSAYILAN (okuma hatasi: " + ex.GetType().Name + " — " + ex.Message + ")";
            }

            GameConfig fallback = new GameConfig();
            fallback.Validate();
            return fallback;
        }
    }
}
