auto.waitFor();

APK_NAME = "抖音";
APP_PACKAGE_NAME = "com.ss.android.ugc.aweme";
// 活动常量
// 抖音主界面活动
MAIN_ACTIVITY = "com.ss.android.ugc.aweme.main.MainActivity";

// 控件常量
// 分享链接前往个人名片id
ID_SHARE_GO = "h0e";
// 抖音个人名片返回键id
ID_PROFILE_BACK = "l6";
// 关注/回关 按钮id
ID_FOLLOW = "hrl";
// 取消关注/互相关注 按钮id
ID_CANCEL_FOLLOW = "hrm";

// 账号uid
UID = 51418577960;
// 需要获取的线索数
USE_FETCH_NUM = 20;
// 本次运行关注的线索数
CURRENT_FOLLOW_NUMS = 0;

// 分享链接前缀
SHARE_URL_PREFIX = "https://www.iesdouyin.com/share/user/";

function follow_process() {
  clues = get_clue();
  for (let i = 0; i < clues.length; i++) {
    clue = clues[i];
    cid = clue["id"];
    uid = clue["userId"];
    share_url = SHARE_URL_PREFIX + uid;
    is_follow = get_user_profile(share_url);
    log(cid + "," + uid + "," + is_follow);
    // http.get('http://47.111.182.11:8989/agent/clue/live_clue/add?is_follow_me='+is_follow+'&uid='+UID+'&clueId='+cid)
    sleep(1000);
    // break
  }
}

function click_by_type(type_name, value) {
  bound = null;
  switch (type_name) {
    case "id":
      bound = id(value).findOne().bounds();
      break;
    case "text":
      bound = id(value).findOne().bounds();
      break;
  }
  click(bound.centerX(), bound.centerY());
}

function get_clue() {
  url =
    "http://47.111.182.11:8989/agent/clue/getLiveClue?uid=" +
    UID +
    "&count=" +
    USE_FETCH_NUM;
  res = http.get(url);
  return res.body.json()["data"]["data"];
}

function get_user_profile(url) {
  recents();
  // 设置分享的链接
  sleep(500);
  setClip(url);
  sleep(1000);
  click(
    text(APK_NAME).findOne().bounds().centerX(),
    text(APK_NAME).findOne().bounds().centerY()
  );
  //   waitForActivity(MAIN_ACTIVITY);
  toastLog("进入抖音主界面");
  id(ID_SHARE_GO).waitFor();
  id(ID_SHARE_GO).click();
  sleep(2000);
  var button_txt = null;
  // 关注操作
  if (!id(ID_CANCEL_FOLLOW).exists()) {
    console.log("关注操作");
    //   id(ID_FOLLOW).click()
    CURRENT_FOLLOW_NUMS++;
    button_txt = id(ID_FOLLOW).findOne().text();
  } else {
    button_txt = id(ID_CANCEL_FOLLOW).findOne().text();
  }
  console.log(button_txt);

  click_by_type("id", ID_PROFILE_BACK);
  if (
    button_txt.indexOf("回关") != -1 ||
    button_txt.indexOf("互相关注") != -1
  ) {
    return 1;
  }
  return 0;
}
follow_process();

console.log(CURRENT_FOLLOW_NUMS);
