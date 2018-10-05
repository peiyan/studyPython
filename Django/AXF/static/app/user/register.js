$(function () {

    flag1 = false;  //表示用户名输入是否合法
    flag2 = false;  //表示密码输入是否合法
    flag3 = false;  //表示确认密码输入是否合法
    flag4 = false;  //表示邮箱输入是否合法

    // 用户名
    // $('#username').change(function () {  # 修改后失去焦点的时候触发,keyup必须是硬键盘,软键盘就不行,blur也可以
    //     var v = $(this).val();   # var 不写就是全局,任何地方都可以使用造成变量污染
    //     if (/^[a-zA-Z_]\w{5,17}$/.test(v)){
    //         // console.log('输入合法');  # 直接alert弹不出来
    //         flag1 = true;
    //     }
    //     else {
    //         // console.log('输入有误');
    //         flag1 = false;
    //     }
    // });

    //用户名
    $('#username').change(function () {
        var v = $(this).val();
        if (/^[a-zA-Z_]\w{5,17}$/.test(v)){
            flag1 = true;

            //如果输入格式正确，则验证用户名是否存在
            $.get('/app/checkusername/', {username: $(this).val()}, function (data) {
                // console.log(data)
                if (data.status == 1) {
                    $('#msg').html('用户名可以使用').css('color', 'green')
                }
                else if (data["status"] == 0) {
                    $('#msg').html(data.msg).css('color', 'red')
                }
                else if (data["status"] == -1) {
                    $('#msg').html('请求方式不正确').css('color', 'red')
                }
            })

        }
        else {
            flag1 = false;
            $('#msg').html('用户名输入有误').css('color', 'orange')
        }
    });

    // 密码
    $('#password').change(function () {
        var v = $(this).val();
        if (/^.{8,}$/.test(v)){
            // console.log('输入合法')
            flag2 = true
        }
        else {
            // console.log('输入有误')
            flag2 = false
        }
    });

    // 确认密码
    $('#again').change(function () {
        if ($(this).val() == $('#password').val()){
            // console.log('输入合法')
            flag3 = true
        }
        else {
            // console.log('输入有误')
            flag3 = false
        }
    });

    // 邮箱
    $('#email').change(function () {
        var v = $(this).val();
        if (/^\w+@\w+\.\w+$/.test(v)){
            // console.log('输入合法')
            flag4 = true
        }
        else {
            // console.log('输入有误')
            flag4 = false
        }
    });


    // 注册
    $('#register').click(function () {

        if (flag1 && flag2 && flag3 && flag4){

            // 表单提交md5加密后的密码
            $('#password').val(md5($('#password').val()));

            return true
        }
        else {
            window.alert('输入有误');
            return false   # 如果是return false 则点击事件无效
        }
    });


    //检测用户名是否存在
    $('#username').change(function () {   # 同时写两个,js会覆盖原来的,jq是可以重复这里的点击事件

        /* JQ中的Ajax  # 封装了js中的xhr

        $.ajax({
            type: 'get',  //可以不写，默认是get
            url: '',  //路径，必须写
            data: {},  //参数
            async: true,  //可以不写，默认是true

            // 请求成功的回调函数
            success: function (data) {
                console.log(data)
            },
            // 请求失败的回调函数
            error: function (err) {
                console.log(err)
            }

        })
        */

        /*
        $.get('url', {}, function (data) {

        })

        $.post('url', {}, function (data) {

        })

        $.getJSON('url', {}, function () {

        })
        */

        /*JS中的Ajax  最原始的,上面的JQ是封装了这个
         *
            var xhr = XMLHttpRequest();
            xhr.open('get', 'url', true)  # true是异步还是同步的参数,异步状态
            xhr.send()
            xhr.onreadystatechange = function () {
                if (xhr.readyState==4 && xhr.status==200){
                    console.log(xhr.responseText)
                }
            }
        */
                                         #  username的引号不用写,参数会放到request请求里面去
        // $.get('/app/checkusername/', {username: $(this).val()}, function (data) {  # 第一个参数是url,反向解析不行,写它相对路径
        //     // console.log(data)
        //     if (data.status == 1) {
        //         $('#msg').html('用户名可以使用').css('color', 'green')
        //     }
        //     else if (data["status"] == 0) {
        //         $('#msg').html(data.msg).css('color', 'red')
        //     }
        //     else {
        //         $('#msg').html('用户名不合法').css('color', 'red')
        //     }
        // })

    })


});