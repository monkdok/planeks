$( document ).ready(function() {

// Functions

function addNewForm(e) {
    e.preventDefault()
    const allColumnsForms = document.getElementsByClassName('item')
    let currentFormCount = allColumnsForms.length
    const columnsForm = document.getElementsByClassName('columns-form')[0]
    const deleteCheckbox = columnsForm.previousSibling.previousSibling
    const copyDeleteCheckbox = deleteCheckbox.cloneNode(true)
    const copyColumnsForm = columnsForm.cloneNode(true)
    const formTarget = document.getElementById('columns-list')
    let allInputs = copyColumnsForm.querySelectorAll(['input', 'select'])
    copyColumnsForm.setAttribute('id', `columns-form-${currentFormCount}`)
    allInputs.forEach(function(el) {
        el.value = ''
        var regex = new RegExp('(-\\d+-)');
        let newColumnId = el.getAttribute('id').replace(regex, `-${currentFormCount}-`)
        let newColumnName = el.getAttribute('name').replace(regex, `-${currentFormCount}-`)
        let newDeleteId = copyDeleteCheckbox.getAttribute('name').replace(regex, `-${currentFormCount}-`)
        let newDeleteName = copyDeleteCheckbox.getAttribute('name').replace(regex, `-${currentFormCount}-`)
        el.setAttribute('id', newColumnId)
        el.setAttribute('name', newColumnName)
        copyDeleteCheckbox.setAttribute('id', newDeleteId)
        copyDeleteCheckbox.setAttribute('name', newDeleteName)
        if (el.getAttribute('name').includes('order'))  {
            el.value = el.value + currentFormCount
        };
    })
    totalForms.setAttribute('value', currentFormCount)
    formTarget.append(copyColumnsForm)
    formTarget.insertBefore(copyDeleteCheckbox, copyColumnsForm)
};


function checkSingleSelected(el) {
    let index = el.selectedIndex;
    let value = el.children[index].value
    let intRange = $(el).closest('div').next('.int_range')[0]
    if(value == 7 || value == 8) {
        $(intRange).attr('hidden', false)
    }
    else {
        $(intRange).attr('hidden', true)
    }
};

function checkAllSelected(){
  $('select').each(function(){
     checkSingleSelected(this)
  })
};


function deleteForm(btn, prefix) {
    $(btn).parents('.item').hide();
    if (prefix != 'None') {
        $('#id_form' + prefix + 'DELETE').prop('checked', true)
        let url = '/delete/column/' + prefix
        $.ajax({
            url: url,
            success: function (data) {
                if (data.error) {
                    alert(data.error)
                    $(btn).parents('.item').show();
                    return
                }
                $(btn).parents('.item').remove();
            },
            type: 'GET'
        }); // End ajax
    } // End IF
};


// Event listeners
const addMoreBtn = document.getElementById('add-columns-form')
let totalForms = document.getElementById('id_form-TOTAL_FORMS')

addMoreBtn.addEventListener('click', addNewForm)

$('body').on('change', 'select', function(){
    checkSingleSelected(this)
});

$("body").on('click', '.remove-form-row',function () {
    if ($('.remove-form-row').length > 1) {
        $('#columns-list').find('input:checkbox:not(:checked)').last().prop('checked', true)
        deleteForm($(this), String($(this).attr('id') || 0));
    };
});

$('#columns-list').find('input:checkbox').each(function(index, elem) {
    $(elem).hide()
})

checkAllSelected()

});