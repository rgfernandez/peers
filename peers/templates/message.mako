${h.form(h.url_for(action='create'), method='POST')}

<table><tr>
    <td>Name (optional):</td>
    <td>
        ${h.text('name')}
    </td>
</tr><tr>
    <td>Phone number:</td>
    <td>
        ${h.text('contact')}
    </td>
</tr><tr>
    <td>Headers:</td>
    <td>
        ${h.textarea('headers')}
    </td>
</tr><tr>
    <td>Message:</td>
    <td>
        ${h.textarea('body')}
    </td>
</tr></table>

${h.submit('submit', 'Submit')}

${h.end_form()}