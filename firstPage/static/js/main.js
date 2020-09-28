$(document).ready(() => {
  // $('#searchForm').on('click', (e) => {

    var searchText = $('#searchText').text();
    // var searchText="money heist"
    console.log("oey :"+searchText);
    getMovies(searchText);
    // e.preventDefault();
  // });
});

function getMovies(searchText){
  axios.get("http://api.tvmaze.com/singlesearch/shows?q="+ searchText)
    .then((response) => {
      console.log(response);
      let movies = response.data;
      let output = '';

        output += `
        <a href="${movies.officialSite}">
          <img class="row__poster" src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Netflix_2015_N_logo.svg/493px-Netflix_2015_N_logo.svg.png' width="50" height="70" alt="netflix"></a>
        `;

        $('#movies').html(output);
      })
      .catch((err) => {
        console.log(err);
      });
  }
  // <div class="well text-center">
  //   <img src="${movies.image.medium}">
  //   <h5>${movies.name}</h5>
