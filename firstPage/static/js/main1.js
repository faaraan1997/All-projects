$(document).ready(() => {
  // $('#searchForm').on('click', (e) => {

    var searchText = $('#searchText1').text();
    // var searchText="money heist"
    console.log("oey :"+searchText1);
    getMovies(searchText);
    // e.preventDefault();
  // });
});

function getMovies(searchText1){
  axios.get("http://api.tvmaze.com/singlesearch/shows?q="+ searchText1)
    .then((response) => {
      console.log(response);
      let movies = response.data;
      let output = '';

        output += `
        <a href="${movies.officialSite}">
          <img class="row__poster" style="margin-right: 10px;" src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Logo_Netflix.png/1200px-Logo_Netflix.png' width="100" height="40" alt="netflix"></a>
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
