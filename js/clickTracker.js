$(document).ready(function(){
    $('a').on('click', function(){
        $.ajax({
            'url' : 'http://localhost:8111',
        })
    });
});
