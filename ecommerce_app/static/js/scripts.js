$(document).ready(function(){
    $('.image-main').slick({
      dots: true,
      arrows: false,
      autoplay: true,
      autoplaySpeed: 2500, 
      infinite: true
    });
  });



  $(document).ready(function(){
    $('.cards-main').slick({
      dots: true,
      arrows: true,
      slidesToShow: 5, 
      slidesToScroll: 1, 
    });
  });