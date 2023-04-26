async function loadanimals() {
      const response = await axios.get('http://localhost:8000/animals')
  
      const animals = response.data
  
      const lista = document.getElementById('animals-list')
  
      lista.innerHTML = ''
  
      animals.forEach(animal => {
          const item = document.createElement('li')
  
          const row = `${animal.name} - idade: ${animal.idade} - color: ${animal.color}`
  
          item.innerText = row
  
          lista.appendChild(item)
      });
  
  }
  
  function manipulateform() {
      const form_animal = document.getElementById('form-animal')
      const input_name = document.getElementById('name')
  
      form_animal.onsubmit = async (event) => {
          event.preventDefault()
          const name_animal = input_name.value
  
          await axios.post('http://localhost:8000/animals', {
              name: name_animal,
              idade: 4,
              sex: 'femea',
              color: 'branco'
          })
  
          loadanimals()
          alert('Animal cadastrado..')
      }
  }
  
  function app() {
      console.log('app started')
      loadanimals()
      manipulateform()
  }
  
  app()