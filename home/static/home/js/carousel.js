$(document).ready(function() {

    $('.home-carousel').carousel({
        'interval': 3000
    });

    $('.home-carousel').on('slide.bs.carousel', function (e) {
        /*
            CC 2.0 License Iatek LLC 2018 - Attribution required
        */
        var $e = $(e.relatedTarget);
        var idx = $e.index();
        var itemsPerSlide = 5;
        var items = $(this).find('.carousel-item');
        var inner = $(this).find('.carousel-inner');
        var totalItems = items.length;
    
        if (idx >= totalItems-(itemsPerSlide-1)) {
            var it = itemsPerSlide - (totalItems - idx);
            for (var i=0; i<it; i++) {
                // append slides to end
                if (e.direction=="left") {
                    items.eq(i).appendTo(inner);
                }
                else {
                    items.eq(0).appendTo(inner);
                }
            }
        }
    });
})
