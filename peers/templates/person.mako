${h.form(h.url_for(action='create'), method='POST')}

<table><tr>
    <td>First Name:</td>
    <td>
        ${h.text('first_name')}
    </td>
</tr><tr>
    <td>Middle Name:</td>
    <td>
        ${h.text('middle_name')}
    </td>
</tr><tr>
    <td>Last Name:</td>
    <td>
        ${h.text('last_name')}
    </td>
</tr><tr>
    <td>Birthdate:</td>
    <td>
        ${h.textarea('birthdate')}
    </td>
</tr><tr>
    <td>Contact:</td>
    <td>
        ${h.text('contact')}
    </td>
</tr></table>

${h.submit('submit', 'Submit')}

${h.end_form()}