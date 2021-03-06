 // Preloader
 $(window).on('load', function() { // makes sure the whole site is loaded 
  $('#status').fadeOut(); // will first fade out the loading animation 
  $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website. 
  $('body').delay(350).css({'overflow':'visible'});
});

// jquery function
$(document).ready(function(){
  // scroll position indicator
  $(window).on('scroll', function() {

    // var docHeight = $(document).height(),
    //     winHeight = $(window).height();

    // var viewport = docHeight - winHeight,
      var positionY = $(window).scrollTop();

    // var indicator = ( positionY / (viewport)) * 100;

    if( positionY > 115) {
          $('.sticky-nav').addClass('sticky')
        } else {
          $('.sticky-nav').removeClass('sticky')
        };
        
    // $('.scroll-bar').css('width', indicator + '%');
      
  });
  // toggle nav
  $(".toggle").on("click", function(){
    if ($(".item").hasClass("active")) {
      $(".item").removeClass("active");
      $(this).find("a").html("<i class='fas fa-bars'></>");
    } else{
      $(".item").addClass("active");
      $(this).find("a").html("<i class='fas fa-times'></>");
    }
  });
  // markdown content image resized to bootstrap card-img-top class
  $(".card-body img").each(function(){
    $(this).addClass("card-img-top");
  });
  // reply btn fadeToggle()
  $(".comment-reply-btn").click(function(event){
    event.preventDefault();
    $(this).parent().next(".comment-reply").fadeToggle();
  });
});