// Pause the video when the modal is closed
$(document).on('click', '.close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
// Show movie details and trailer when modal is opened
$(document).on('click', '.movie-tile', function (event) {
    // Show title and storyline
    var titleStr = $(this).attr("data-title");
    var storylineStr = $(this).attr("data-storyline");
    $(".modal-title").html(titleStr);
    $("#storyline-container").html(storylineStr);

    // Start playing the video whenever the trailer modal is opened
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});
// Animate in the movies when the page loads
$(document).ready(function () {
    $('.movie-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });
});