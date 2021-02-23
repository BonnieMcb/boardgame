console.log("Staff JS loaded.")

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

        $('#product_ids').val('');
        $('#delete-contents').html('');

        allIds = [];

        checked.each(function() {

            let col = $(this).parent();

            // add to the product id form
            let id = col.siblings('.game-id').text();
            allIds.push(id);

            // add to the modal
            let name = col.siblings('.game-name').text();
            let singleItem = "<div>" + name + "</div>";
            $('#delete-contents').append(singleItem);
        });

        // set up the ids
        $('#product_ids').val(allIds.join(','));
        
        let delText = checked.length + " ITEM" + (checked.length > 1 ? "S" : "");
        $('#delete-text').html(delText)

        $('.modal').modal();
    });
});
