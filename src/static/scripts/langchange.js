import languages from '../json/lang/lang.json'assert { type: 'json' };

function changeLanguage(lang,obj,subobj){
    console.log(languages[lang][obj][subobj]);

};

let Button = document.getElementById("changelang-btn");

Button.onclick = function(){
    changeLanguage('en_US','navbar','met-label');
}