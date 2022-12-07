django.jQuery().ready(function(){
    django.jQuery("#id_estado").on('change', function(e) {
        django.jQuery("#id_cidade option").remove();
        django.jQuery("#id_cidade").append("<option value>---------</option>");
        if (e.target.value != "") {
            django.jQuery.ajax({
                method: 'get',
                url: '/api/cidades/'+e.target.value,
                success: (res) => {
                    JSON.parse(res).forEach(cidade => {
                        django.jQuery("#id_cidade").append(`
                        <option ${cidade.fields.capital ? 'selected' : ''} 
                        value=${cidade.pk}>${cidade.fields.nome}
                        </option>
                        `);
                    });
                }
            });
        }
    });
});
