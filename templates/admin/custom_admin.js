// Arquivo: static/admin/js/custom_admin.js
(function ($) {
    $(document).ready(function () {
        // Evento ao clicar no botão "Adicionar outro" no formulário inline
        $('.add-row').on('click', function () {
            // Obtém o valor selecionado do campo de meta
            var metaId = $('#id_meta').val();

            // Adiciona o valor ao link do botão "Adicionar outro"
            var addAnotherLink = $('.add-another').attr('href');
            if (addAnotherLink) {
                addAnotherLink += '&meta=' + metaId;
                $('.add-another').attr('href', addAnotherLink);
            }
        });
    });
})(django.jQuery);
