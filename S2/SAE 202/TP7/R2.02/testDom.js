 
      // ---------------- Conditions iniales
      document.querySelector('#div').value="";  let clearDiv=true;
      document.querySelector('#p').value="";    let clearP=true;
      // ---------------- nb div
      document.querySelector('#nb_div').addEventListener('click',nbDiv);
      function nbDiv() {
        nb = document.querySelectorAll('div').length;
        document.querySelector('#div').value=nb;
        if(clearDiv) {
          for(let i=0; i<nb; i++)
            document.querySelectorAll('div')[i].style.backgroundColor='yellow';
        } else {
          for(let i=0; i<nb; i++)
            document.querySelectorAll('div')[i].style.backgroundColor='white';
          document.querySelector('#div').value="";
        }
        clearDiv = (clearDiv===false) ? true : false; 
      }
      // ---------------- fin nb div
      // ---------------- nb p
      document.querySelector('#nb_p').addEventListener('click',nbP);
      function nbP() {
        nb = document.querySelectorAll('p').length;
        document.querySelector('#p').value=nb; 
        if(clearP) {
          for(let i=0; i<nb; i++)
            document.querySelectorAll('p')[i].style.backgroundColor='cyan';
        } else {
          for(let i=0; i<nb; i++)
            document.querySelectorAll('p')[i].style.backgroundColor='white';
            document.querySelector('#p').value="";
        }
        clearP = (clearP===false) ? true : false; 
      }
      // ---------------- fin nb div
      // ---------------- TD
      let texte = "X";
      let indice = -1;
      document.querySelector('table').addEventListener('click', function(event) {
        let cellule = event.target;
        // ----------- 
        texte = cellule.textContent;
        document.querySelector('#c_td').value=texte;
        // ----------- trouver l'indice 
        document.querySelectorAll('td').forEach(function(currentValue, currentIndex, obj) {
          //console.log('currentValue = '+currentValue.textContent+' :: currentIndex = '+currentIndex+' :: texte = ' + texte);
          if(currentValue.textContent === texte) {
            indice = currentIndex;
          }
          if(indice!=-1)
          document.querySelectorAll('td')[indice].style.backgroundColor='yellow';
          //console.log('currentValue = '+currentValue.textContent+' :: currentIndex = '+indice+' :: texte = ' + texte);
        });
        document.querySelector('#pos_td').value=indice;
        
        // ----------- Affecter une classe à la cellule sur laquelle on clique 
        if(document.querySelector('.pos')!==null) {
          document.querySelector('.pos').style.backgroundColor='purple';
          document.querySelector('.pos').className='';
        }
        cellule.className='pos';
        cellule.style.backgroundColor='yellow';
      });
