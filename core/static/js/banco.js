//exemplo
django.jQuery().ready(function(){
    django.jQuery("#id_codigo").on('keyup', function(e) {
        console.log(e.target.value);
    });
});
