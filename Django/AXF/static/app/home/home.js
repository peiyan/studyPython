$(function () {

    // 轮播
    new Swiper('#topSwiper', {  # 比较原代码这里去掉了var+变量名
         loop: true,
         pagination: '.swiper-pagination',  # 这里改变了一些写法,下面有注释的原Demo可以比较

    });

    // 必购
    new Swiper('#swiperMenu', {
        slidesPerView: 3,   # 这里不需要分页器就没写上面的分页器的js,所以必购里面就没显示分页
    })
	
	// 本来的原生代码有var,可以给去掉
	// var mySwiper = new Swiper('.swiper-container',{
	// loop:true,
	// 如果需要分页器
    // pagination: {
    // el: '.swiper-pagination',
    // },
	// });

});   # 里面的function 相当于 on ready 加载完之后调用,它放在网页的最下方
