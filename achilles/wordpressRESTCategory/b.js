fetch('https://dummy-json.mock.beeceptor.com/posts/3')
  .then(response => response.json())
  .then(data => {
    data.categories = [{
        "id": 456,
        "name": "My Category",
        "slug": "my-category"
      }]
    const categories = data.categories;
    console.log(data)
    console.log(categories)
  })
  .catch(error => console.error('Error:', error));

