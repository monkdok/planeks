$(document).ready(function() {
    let dataSetsCount = $('.rows').length
    $('#generate-form').submit(function(e) {
        e.preventDefault()
        let form = $(this)
        let url = form.attr('data-create-schema-url')
        let rows_num = form.find('input[name="rows_num"]').val()
        $.ajax({
            url: url,
            success: function (data) {
                let date = data['created_dt']
                let datasetId = data['dataset_id']
                ++dataSetsCount
                let row = '<tr><th scope="row">' + dataSetsCount + '</th><td>' + date + '</td><td id="'
                 + dataSetsCount + '"><span class="badge text-bg-secondary">Processing</span></td></tr>'
                $('.datasets').append(row)
                let generateUrl = form.attr('action')
                $.ajax({
                    url: generateUrl,
                    data: {
                        'rows_num': rows_num,
                        'dataset_id': datasetId,
                    },
                    success: function (data) {
                        let datasetUrl = data['dataset_url']
                        if (datasetUrl) {
                            $('#' + dataSetsCount).text('Ready')
                            row = '<tr><th scope="row">' + dataSetsCount + '</th><td>' + date + '</td><td id="'
                            + dataSetsCount + '"><span class="badge text-bg-success">Ready</span></td><td><a href="'
                            + datasetUrl + '">Download</a></td></tr>'
                            $('#' + dataSetsCount).parent().replaceWith(row)

                            $('.datasets rows:last').replaceWith(row)
                        }
                    }
                }) // end of ajax
            },
        }) // end of ajax
    }) // end generate-form submit event
})