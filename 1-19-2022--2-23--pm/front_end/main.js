var date = new Date();
var carYearMax = date.getFullYear()+1;
var mobile = false;

document.getElementById('vehicle_year').max = carYearMax;

if($.browser.device = (/android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(navigator.userAgent.toLowerCase()))){
    location.replace("https://www.w3schools.com");
}