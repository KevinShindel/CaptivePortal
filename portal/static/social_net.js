"use strict"

$( ".focus, .inline" ).on('click', function () { //Ловим клик и ID-кнопки
    var net_name = $(this).attr("data-id");
    alert(net_name+' PRESSED!')
});

//
// $('.show_popup').click(function() {                      // Вызываем функцию по нажатию на кнопку
//     var popup_id = $('#' + $(this).attr("rel")); // Связываем rel и popup_id
//     $(popup_id).show();                                 // Открываем окно
//     $('.overlay_popup').show();                         // Открываем блок заднего фона
// })
// $('.overlay_popup').click(function() {                  // Обрабатываем клик по заднему фону
//     $('.overlay_popup, .popup').hide();                 // Скрываем затемнённый задний фон и основное всплывающее окно
// })