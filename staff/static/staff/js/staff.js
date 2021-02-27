$(document).ready(function() {

    let all = $('.delete-check');
    let deleteBtn = $('#delete-btn');

    // activate/deactivate delete button when selecting rows
    all.on('change', function() {

        let anyChecked = all.is(':checked');
        deleteBtn.prop('disabled', !anyChecked);
    });

    // populate confirmation modal with data
    deleteBtn.on('click', function() {

        let checked = $('.delete-check:checked');

        $('.remove_ids').val('');
        $('#delete-contents').html('');

        allIds = [];

        checked.each(function() {

            let col = $(this).parent();

            // add to the id form
            let id = col.siblings('.game-id').text();
            allIds.push(id);

            // add to the modal
            let name = col.siblings('.game-name').text();
            let singleItem = "<div>" + name + "</div>";
            $('#delete-contents').append(singleItem);
        });

        // set up the ids
        $('.remove_ids').val(allIds.join(','));
        
        let delText = checked.length + " ITEM" + (checked.length > 1 ? "S" : "");
        $('#delete-text').html(delText)

        $('.modal').modal();
    });

    // toggle all checkboxes for easy bulk deletion
    $('#check-all').on('click', function() {

        let checked = $(this).is(':checked');
        all.attr('checked', checked);

        all.change();
    });

    // datepicker for event editing
    $('input[name=datetime]').flatpickr({
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        minDate: 'today'
    });

    // category/mechanic editing
    $('.single-item').on('input', function() {
        
        // find the target buttons
        let cancelBtn = $(this).parent().parent().siblings().children('.btn-cancel');
        let confirmBtn = $(this).parent().parent().siblings().children('.btn-confirm');

        let defaultVal = $(this).attr('default');
        let currentVal = $(this).val();

        if (defaultVal == currentVal) {
            cancelBtn.attr('disabled', true);
            confirmBtn.attr('disabled', true);
            return;
        }

        cancelBtn.attr('disabled', false);
        confirmBtn.attr('disabled', false);
    })

    $('.btn-cancel').on('click', function() {

        // find the input
        let input = $(this).parent().siblings().find('.single-item');
        input.val(input.attr('default'));

        input.trigger('input');
    });

    $('.btn-confirm').on('click', function() {

        // find the right form to submit
        let form = $(this).parent().siblings().find('form');
        form.submit();
    });
});
