function sendToServer()
{
        const formData = this.buildForm();
        axios.post('http://localhost:2000/record', formData)
          .then(response => console.log(response));
}

var pusher = new Pusher('APP-KEY', {
      cluster: 'CLUSTER',
      encrypted: true
    });