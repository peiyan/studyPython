$.getJSON('/api/v1/wheel/', function (response) {
    if (response['status'] == 200){
        var wheelArr = response['data']

        // ol父元素
        var $indicators = $('.carousel-indicators')
        var $inner = $('.carousel-inner')

        for (var i=0; i<wheelArr.length; i++){
            // 创建子元素li
            var $li;
            var $item;

            if (i == 0){
                // 小圆点
                $li = $('<li></li>').attr('data-target', '#carousel-example-generic').attr('data-slide-to', i).addClass('active')

                 // 图片
                $item = $('<div></div>').addClass('item active')
                var $img = $('<img/>').attr('src', wheelArr[i].img)
                $item.append($img)
            } else {
                $li = $('<li></li>').attr('data-target', '#carousel-example-generic').attr('data-slide-to', i)

                $item = $('<div></div>').addClass('item')
                var $img = $('<img/>').attr('src', wheelArr[i].img)
                $item.append($img)
            }

            // 添加到父元素
            $indicators.append($li)
            $inner.append($item)

        }
    }
})