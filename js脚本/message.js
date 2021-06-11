auto.waitFor();

APK_NAME = "抖音";

// 当前登录账号
UID = "101535967615";
// 活动常量
// 抖音主界面活动
MAIN_ACTIVITY = "com.ss.android.ugc.aweme.main.MainActivity";

// 消息列表的头像id
ID_AVATAR = "yq";
// 发送时间的id
ID_SEND_MESSAGE = "gg6";
// 消息对话框的id
ID_MESSAGE_BOX = "gg8";
// 消息对话最上面的关注按钮
ID_CHAT_FOLLOW = "d4y";
// 消息对话框左上角的返回按钮
ID_CHAT_BACK = "fan";
// 个人资料的头像id
ID_PROFILE_AVATAR = "d19";
// 抖音个人名片返回键id
ID_PROFILE_BACK = "l6";
// 资料页面id
ID_PROFILE = "hrz";
// 消息编辑框的id
ID_EDIT_TEXT = "gg2";
// 关注/回关 按钮id
ID_FOLLOW = "hrl";
// 取消关注/互相关注 按钮id
ID_CANCEL_FOLLOW = "hrm";

// 消息框的类
CLASS_MEAASGE_ITEM = "com.bytedance.ies.dmt.ui.widget.DmtTextView";
// 遍历结束时对应的一个类
CLASS_END_CAHRGE = "android.widget.FrameLayout";
// 对话列表的recycle
CLASS_CHAT_VIEW = "androidx.recyclerview.widget.RecyclerView";
// 对话框的类
CLASS_SEND_MESSAGE = "android.widget.TextView";
// 个别输入框需要点击此控件后显示
CLASS_IMAGE_TEXT = "android.widget.ImageView";

// 需要过滤的昵称
EXCLUDE_NICKS = [
  "抖音小助手",
  "系统消息",
  "直播小助手",
  "抖+助手",
  "购物助手",
  "钱包服务助手",
];
// 需要过滤的文本
EXCLUDE_TEXT = [
  "温馨提示",
  "涉及私下交易",
  "撤回",
  "成为好友",
  "回个招呼",
  "消息免打扰",
  "互关朋友可以看到对方的活跃状态",
];

// 粘贴按钮的位置坐标
PASTE_X = 110;
PASTE_Y = 2135;

// 辽宁省的主要城市
LIAONING_PROVINCES = [
  "沈阳",
  "大连",
  "鞍山",
  "抚顺",
  "本溪",
  "丹东",
  "锦州",
  "营口",
  "阜新",
  "辽阳",
  "盘锦",
  "铁岭",
  "朝阳",
  "葫芦岛",
  "兴城",
  "海城",
];

// 粉丝私信发送的话术
FANS_SEND_MESSAGE = "";
// 关注的粉丝数
CURRENT_FANS_FOLLOW_NUM = 0;
// 被动私信关注的人数
CURRENT_PASSIVE_FOLLOW_NUM = 0;
// 回复的人数
REPLY_NUM = 0;

waitForActivity(MAIN_ACTIVITY);
id(ID_AVATAR).waitFor();
toastLog("已进入消息列表界面");
message_check();
console.log(
  "回复数：" +
    REPLY_NUM +
    ",关注的粉丝数：" +
    CURRENT_FANS_FOLLOW_NUM +
    ",被动私信关注的人数：" +
    CURRENT_PASSIVE_FOLLOW_NUM
);

function message_check() {
  // 记录所有昵称
  nicks_all = [];

  out: while (true) {
    // 找到所有的对话列表
    messages = className(CLASS_MEAASGE_ITEM).depth("18").find();
    // 遍历对话列表
    for (let i = 0; i < messages.size(); i++) {
      // 对方是否关注当前账号
      is_follow_me = null;

      messages = className(CLASS_MEAASGE_ITEM).depth("18").find();

      // 官方账号过滤
      /**
       * 因为更新版本，这部分控件已经发生变化，不需要再判断
       * if (
        messages.get(i).child(0).child(1).child(0).child(0).childCount() > 2 &&
        messages.get(i).child(0).child(1).child(0).child(0).child(1).text() ==
          "官方"
      ) {
        continue;
      }
       */

      // 获得昵称
      var nick = messages
        .get(i)
        .child(0)
        .child(1)
        .child(0)
        .child(0)
        .child(0)
        .text();

      // 进一步过滤特定账号
      if (nicks_all.indexOf(nick) != -1 || EXCLUDE_NICKS.indexOf(nick) != -1) {
        continue;
      }

      log(nick);
      nicks_all.push(nick);

      // 点击第i个对话框
      messages.get(i).click();
      sleep(1000);

      // 记录上一次遍历时消息总长度
      var pre_content_length = 0;
      // 本次遍历长度
      var current_content_length = 0;

      // 读取到的一句话
      msg = null;
      // 记录所有信息
      msg_all = [];
      // 记录两边的语句数量
      left_count = 0;
      right_count = 0;

      //此处遍历某个人的消息记录
      while (true) {
        // 列表对象
        message_items = className(CLASS_CHAT_VIEW).findOne().children();
        // 存放一页的信息
        temp_msg = [];

        for (let j = 0; j < message_items.size(); j++) {
          // 获得列表的所有子对象
          messageItem = message_items.get(j);

          if (
            // 版本更新消息对话框出现了视频推荐需要过滤
            messageItem.childCount() == 1 ||
            messageItem.childCount() > 3
          ) {
            continue;
          }

          // 判断有没有时间
          if (messageItem.child(0).child(0) != null) {
            msg = messageItem.child(0).child(0).text();
            // 字符串前缀拼接表示时间
            prefix_msg = "time::" + msg;
            if (msg_all.indexOf(prefix_msg) == -1) {
              temp_msg.push(prefix_msg);
              current_content_length++;
            }
          }
          //系统提示信息过滤
          flag = false;
          for (index in EXCLUDE_TEXT) {
            if (
              messageItem.child(1).text().indexOf(EXCLUDE_TEXT[index]) != -1
            ) {
              flag = true;
              break;
            }
          }
          if (flag) continue;

          // 通过头像坐标区分发送消息的对象
          if (
            messageItem.child(1).child(0).bounds().centerX() <
            device.width / 2
          ) {
            if (
              messageItem
                .child(1)
                .child(1)
                .child(0)
                .child(0)
                .child(0)
                .child(0) != null
            ) {
              msg = messageItem
                .child(1)
                .child(1)
                .child(0)
                .child(0)
                .child(0)
                .child(0)
                .text();
            } else {
              msg = messageItem
                .child(1)
                .child(1)
                .child(0)
                .child(0)
                .child(0)
                .text();
            }

            // 字符串前缀拼接表示对方话术
            prefix_msg = "msg1::" + msg;
            if (msg_all.indexOf(prefix_msg) == -1 && msg != "") {
              temp_msg.push(prefix_msg);
              current_content_length++;
              left_count++;
            }
          } else {
            msg = messageItem
              .child(1)
              .child(0)
              .child(0)
              .child(0)
              .child(0)
              .text();
            // 字符串前缀拼接表示当前账号发出的话术
            prefix_msg = "msg0::" + msg;
            if (msg_all.indexOf(prefix_msg) == -1) {
              temp_msg.push(prefix_msg);
              current_content_length++;
              right_count++;
            }
          }
        }
        if (temp_msg.length) {
          msg_all = temp_msg.concat(msg_all);
        }

        // 一个对话遍历结束标志
        if (current_content_length == pre_content_length) {
          break;
        }
        pre_content_length = current_content_length;

        swipe_list();
        sleep(1000);
      }
      log(msg_all);
      log(left_count + "," + right_count);

      /**
       * 如果没有关注对方
       * 说明是被动私信 或者 粉丝直接私信
       */
      if (id(ID_CHAT_FOLLOW).exists()) {
        // 粉丝私信，因为给他发过信息，需要这边关注，返回接口信息
        if (right_count > 0 && msg_all.indexOf(FANS_SEND_MESSAGE) != -1) {
          log("粉丝私信");
          result = copy_share_url();
          CURRENT_FANS_FOLLOW_NUM++;
          share_url = result[0];
          is_follow = result[1];
          console.log(share_url + "," + is_follow);
          // http.get(
          //   "http://47.111.182.11:8989/agent/clue/add?share_url=" +
          //     share_url +
          //     "&is_follow_me=" +
          //     is_follow +
          //     "&send_message=" +
          //     msg_all +
          //     "&uid=" +
          //     UID +
          //     "&message_type=2"
          // );
          back();
          sleep(500);
        } else {
          log("被动私信");
          // 获得资料卡片的地址信息
          location = null;
          desc("更多").click();
          sleep(500);
          click_by_type("id", ID_PROFILE_AVATAR, 0);
          id(ID_PROFILE).waitFor();
          var location_obj = className(CLASS_SEND_MESSAGE)
            .depth("17")
            .drawingOrder("2")
            .findOne(2000);
          if (location_obj == null || location_obj.text() == "暂时没有更多了") {
            location = null;
          } else if (location_obj.text() == id("gsj").findOne().text()) {
            location = null;
          } else {
            location = location_obj.text();
          }
          log(location);
          desc("返回").click();
          sleep(500);
          desc("返回").click();
          sleep(500);
          // 如果是辽宁则关注
          if (
            location != null &&
            (location.indexOf("辽宁") != -1 || city_check(location))
          ) {
            result = copy_share_url();
            share_url = result[0];
            is_follow = result[1];
            console.log(share_url + "," + is_follow);
            CURRENT_PASSIVE_FOLLOW_NUM++;
            // http.get(
            //   "http://47.111.182.11:8989/agent/clue/add?share_url=" +
            //     share_url +
            //     "&is_follow_me=" +
            //     is_follow +
            //     "&send_message=" +
            //     msg_all +
            //     "&uid=" +
            //     UID +
            //     "&message_type=1"
            // );
            back();
            sleep(500);
          } else {
            id(ID_CHAT_BACK).click();
            sleep(500);
            continue;
          }
        }
      } else {
        // 说明已经关注对方，此处给接口返回消息，返回
        /**
         * 回复数暂时就用左边对话的数是否大于0 判断
         */
        if (left_count > 0) {
          REPLY_NUM++;
        }
        log("已关注对方");
        desc("更多").click();
        sleep(500);
        click_by_type("id", ID_PROFILE_AVATAR, 0);
        id(ID_PROFILE).waitFor();
        sleep(500);
        desc("更多").findOne().click();
        sleep(500);
        desc("分享，按钮").click();
        sleep(500);
        click_by_type("id", "j10", 0);

        desc("返回").click();
        sleep(500);
        desc("返回").click();
        sleep(800);
        swipe(
          device.width / 2,
          (device.height * 5) / 6,
          device.width / 2,
          device.height / 3,
          500
        );
        if (className(CLASS_IMAGE_TEXT).depth("8").drawingOrder("1").exists()) {
          // log(className(CLASS_IMAGE_TEXT).depth('8').drawingOrder('1').find().size())
          className(CLASS_IMAGE_TEXT)
            .depth("8")
            .drawingOrder("1")
            .findOne()
            .click();
        }
        press(
          id(ID_EDIT_TEXT).findOne().bounds().centerX(),
          id(ID_EDIT_TEXT).findOne().bounds().centerY(),
          1000
        );
        click(PASTE_X, PASTE_Y);
        share_url = id(ID_EDIT_TEXT).findOne().text();
        setText("");
        sleep(500);
        console.log(share_url);
        // http.get(
        //   "http://47.111.182.11:8989/agent/clue/addReply?uid=" +
        //     UID +
        //     "&message=" +
        //     msg_all +
        //     "&share_url=" +
        //     share_url
        // );
        back();
        sleep(500);
      }
      //TODO 给接口返回信息

      sleep(1000);
    }
    swipe(
      device.width / 2,
      (device.height * 5) / 6,
      device.width / 2,
      device.height / 3,
      500
    );
    // 遍历结束判断
    if (
      className(CLASS_END_CAHRGE).depth("18").drawingOrder("11").exists() &&
      className(CLASS_END_CAHRGE)
        .depth("18")
        .drawingOrder("11")
        .findOne()
        .childCount() == 1 &&
      className(CLASS_END_CAHRGE)
        .depth("18")
        .drawingOrder("11")
        .findOne()
        .child(0)
        .text() == "暂时没有更多了"
    )
      break out;
  }
}

function click_by_type(type_name, value, order) {
  bound = null;
  switch (type_name) {
    case "id":
      bound = id(value).find().get(order).bounds();
      break;
    case "text":
      bound = text(value).find().get(order).bounds();
      break;
    case "desc":
      bound = desc(value).find().get(order).bounds();
  }
  click(bound.centerX(), bound.centerY());
}

function swipe_list() {
  swipe(
    device.width / 2,
    device.height / 3,
    device.width / 2,
    (device.height * 5) / 6,
    500
  );
}

// 这个函数调用的前提是在消息对话界面内
function copy_share_url() {
  desc("更多").click();
  sleep(500);
  click_by_type("id", ID_PROFILE_AVATAR, 0);
  id(ID_PROFILE).waitFor();
  sleep(500);
  var button_txt = null;
  var is_secret = false
  // 关注操作
  // 判断对方关注情况
  if (!id(ID_CANCEL_FOLLOW).exists()) {
    console.log("关注操作");
    //   id(ID_FOLLOW).click()
    button_txt = id(ID_FOLLOW).findOne().text();
  } else {
    button_txt = id(ID_CANCEL_FOLLOW).findOne().text();
  }
  console.log(button_txt);
  is_follow = 0;
  if (
    button_txt.indexOf("回关") != -1 ||
    button_txt.indexOf("互相关注") != -1
  ) {
    is_follow = 1;
  }
  // 获得分享链接
  if (!text('这是私密账号').exists()){
    desc("更多").findOne().click();
    sleep(500);
    desc("分享，按钮").click();
    sleep(500);
    click_by_type("id", "j10", 0);
  }else {
    is_secret = true
  }


  desc("返回").click();
  sleep(500);
  desc("返回").click();
  sleep(800);
  if (!is_secret){
    
  }
  swipe(
    device.width / 2,
    (device.height * 5) / 6,
    device.width / 2,
    device.height / 3,
    500
  );
  if (className(CLASS_IMAGE_TEXT).depth("8").drawingOrder("1").exists()) {
    className(CLASS_IMAGE_TEXT).depth("8").drawingOrder("1").findOne().click();
  }
  press(
    id(ID_EDIT_TEXT).findOne().bounds().centerX(),
    id(ID_EDIT_TEXT).findOne().bounds().centerY(),
    1000
  );
  click(PASTE_X, PASTE_Y);
  share_url = id(ID_EDIT_TEXT).findOne().text();
  setText("");
  sleep(500);
  return [share_url, is_follow];
}

function city_check(location_name) {
  for (let i = 0; i < LIAONING_PROVINCES.length; i++) {
    if (location_name.indexOf(LIAONING_PROVINCES[i]) != -1) {
      return true;
    }
  }
  return false;
}
