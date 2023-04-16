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

const form =  document.querySelector("#search-input");
const li = document.querySelector(".li-prod")

form.addEventListener("input", function(event){
	const formSearch = document.querySelector('.form-search');
  	const formData = new FormData(formSearch);
  	const csrfToken = formData.get('csrfmiddlewaretoken');

  	formData.append('csrfmiddlewaretoken', csrfToken);

 	url = "/searchForm/";
  	fetch(url, {
  	  method: 'POST',
  	  headers: {
  	    'X-CSRFToken': csrfToken
  	  },
  	  body: JSON.stringify({
  	    'querry': form.value,
  	  }),
	}).then(data =>{
		console.log(data.body)
		// li.innerHTML = JSON.parse(data)
	})
})	