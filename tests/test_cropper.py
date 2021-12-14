from publisher.commute.cropper import cut_out_pdf


def test_cut_out_pdf(document_name_cropper):
    total_height: float = 16.0
    width: float = 6.292546341584
    write_pdf = document_name_cropper

    response = cut_out_pdf(document_name=document_name_cropper, total_height=total_height, width=width, write_pdf=write_pdf)
