$(function(){
    // 获取到元素中的字体，设置字体基数  是屏幕宽度的十分之一 
	// fontSize   px,em（相对于父元素）， rem （相对于根元素的） 
	// 默认 1em和1rem都是16px,px也行,rem可以随着手机的大小做相应的改变
	// 1rem在这里相当于宽度的10之一,10rem相当于屏幕的100%
	// 这里规定了1/10所以,没有默认
    document.documentElement.style.fontSize = innerWidth / 10 + "px";
	// innerWidth/10 把屏幕给分成10份,rem就相当于1/10
})