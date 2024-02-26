---
title: CSP Final
categories: ['CSP', 'Week 21']
tags: ['hacks']
---

<!-----



Conversion time: 0.448 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Sun Feb 25 2024 21:12:11 GMT-0800 (PST)
* Source doc: team review
* Tables are currently converted to HTML tables.
----->



# Features Prior to Implementation

Description of features prior to implementation:



* Design and planning
* Key features
* [Features prior to implementation](https://kinetekenergy.github.io/blog/posts/Checkpoint_IPYNB_2_/)

Planning table of issues and features:


<table>
  <tr>
   <td><strong>Issue</strong>
   </td>
   <td><strong>Solution</strong>
   </td>
  </tr>
  <tr>
   <td>View counter was not updating.
   </td>
   <td>The HTML request had to be a <code>PUT</code> so that it could update the view count. It should then commit to <code>db</code> with <code>db.commit()</code>
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/240de7cd9cf8040637bb87eec5bf8264565cab1b">Fix</a>
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3">Issue</a>
   </td>
  </tr>
  <tr>
   <td>Return errors were all messed up and weren’t returning the correct error code (this error actually showed up during a live review but was fixed on-the-fly).
   </td>
   <td>The <code>return</code> code allows you to choose the error. This needed to be set properly because we had messed up the codes. 
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/6352cfac8f3f499751d44ce573be3aadc324f4fb">Fix</a>
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3">Issue</a>
   </td>
  </tr>
  <tr>
   <td>Adding a video would be NULL and the video id in the URL wouldn’t work.
   </td>
   <td>Code was reordered so that the video id was put properly: <code>self._videoID = self.id</code> was changed to be last so that the video id is updated last and isn’t changed.
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410">Fix</a>
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410">Issue</a>
   </td>
  </tr>
  <tr>
   <td>Users could add random text for emails and junk text.
   </td>
   <td>A filter was added so that emails must contain an “@” symbol as well as being over five characters.
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/29073c9a91fa89dc4b7ab29a261e13d296cda4a3">Fix</a>
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410">Issue</a>
   </td>
  </tr>
  <tr>
   <td>Video thumbnails were not working.
   </td>
   <td>The image in the backend is stored as a base64 and is sent to the front end. However, there were issues in the javascript decoding. To fix this, a <code>regex</code> was implemented so that the base64 is cleaned up and is displayed properly.
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-frontend/commit/bbce2f295fe3414cd2a97ae3b756fe65d57ffc87">Fix</a>
<p>
<a href="https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410">Issue</a>
   </td>
  </tr>
</table>

Features:

<table>
  <tr>
   <td><strong>Features</strong>
   </td>
   <td><strong>Link</strong>
   </td>
  </tr>
  <tr>
   <td>View count which updates whenever someone views a video
   </td>
   <td rowspan="5" ><a href="https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3">Issue</a>
   </td>
  </tr>
  <tr>
   <td>Video categories to sort videos and choose which category to watch
   </td>
  </tr>
  <tr>
   <td>Login feature which connects to upload. When uploading a video, the user who uploaded it will be in the description and this will be automatic.
   </td>
  </tr>
  <tr>
   <td>Deleting user accounts and updating an email so that users can close their account and update information
   </td>
  </tr>
  <tr>
   <td>Allow users to add a description to their videos. They can also add a tag so that the category feature sorts it
   </td>
  </tr>
</table>


