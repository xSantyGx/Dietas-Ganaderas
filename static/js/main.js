const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete){
    const arreglobtn = Array.from(btnDelete);
    arreglobtn.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('¿Desea eliminar el dato?')){
                e.preventDefault();
            }
        });
    });
}