/**
 * 语音识别服务aksk 方式请求的使用示例
 */
var sentence = require("./ais_sdk/asr_sentence");
var utils = require("./ais_sdk/utils");

var app_key = "*************";
var app_secret = "************";

var filepath = "./data/asr-sentence.wav";
var data = utils.changeFileToBase64(filepath);

obsUrl = "https://ais-sample-data.obs.myhuaweicloud.com/asr-sentence.wav";

sentence.asr_scentence_aksk(app_key, app_secret, data, "", "wav", "16k", function (result) {
    console.log(result);
    console.log(JSON.parse(result).result.words)
});

sentence.asr_scentence_aksk(app_key, app_secret, "", obsUrl, "wav", "16k", function (result) {
    console.log(result);
    console.log(JSON.parse(result).result.words)
});