Dim Word
Dim WordDoc

set Word = CreateObject("Word.Application")
Set WordDoc = Word.Documents.open ("C:\Dev\macro\a.docx")
Word.Visible = True

Dim objAddin
objAddin = Word.AddIns.Add ("\totalclean.dotm", True)
Set Text = WordDoc.content

Word.Run ("Text total clean")
Word.AddIns("C:\Dev\macro\macro.dotm").Delete

Word.ActiveDocument.SaveAs ("C:\Dev\macro\b.docx")
WordDoc.Close ()
Word.Quit True