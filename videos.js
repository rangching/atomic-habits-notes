// ============================================================
//  影片連結（由 site_writeback.py 自動回寫，也可以手動改）
//  youtube ：影片 ID 或網址      short  ：直式重點版（Shorts）ID
//  duration：片長 "6:35"          sections：各小節開始秒數（數量＝小節數），null 用 content.js 預估
//  noVoice ：無旁白版 ID          mp4    ：自架 MP4（沒有 YouTube 時才用）
// ============================================================

window.SERIES_PLAYLIST = ""; // 系列播放清單網址（公開或不公開後才填）
window.SERIES_TRAILER = "";  // 系列前導片 ID（延續型系列）

window.VIDEO_LINKS = {
  u01: { youtube: "rc-uCuw9TXg", mp4: "", duration: "11:44", sections: [0, 103.3, 210.3, 294.9, 357.8, 459, 539.1, 576.1], noVoice: "", short: "" },
  u02: { youtube: "txq9Fw8ZPOo", mp4: "", duration: "13:50", sections: [0, 143.5, 213.3, 294.8, 393, 519.1, 650.6, 709.8], noVoice: "", short: "" },
  u03: { youtube: "hptvWFdGi60", mp4: "", duration: "13:43", sections: [0, 125.6, 205, 301.2, 420.8, 485.2, 600, 688], noVoice: "", short: "" },
  u04: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u05: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u06: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u07: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u08: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u09: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u10: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u11: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" }
};
