from colored import fg, bg, attr

def getAsciiWizard():
    wizard = """\
                            {black}      {reset}
                        {black}     {reset}{yellow}    {reset}{black}  {reset}
                    {black}  {reset}{yellow}      {reset}{orange}  {reset}{black}  {reset}
                    {black}   {reset}{yellow}      {reset}{orange}  {reset}{black}  {reset}
                {black}   {reset}{yellow}cccccc{reset}{orange}eeaaaa{reset}{black}  {reset}
    {black}            {reset}{yellow}cccccc{reset}{orange}eeaaaaaaa{reset}{black}  {reset}
{black}   {reset}{yellow}ccccccccccccccc{reset}{orange}aaaaaaaaaa{reset}{black}  {reset}
    {black}   {reset}{yellow}aaaaaaa{reset}{orange}eeceeeeeg{reset}{black}  {reset}
    {black}      {reset}{yellow}aaaaaaaa{reset}{orange}eeeeeeg{reset}{black}  {reset}
        {black}        {reset}{yellow}aaaaaa{reset}{orange}eeegg{reset}{black}  {reset}
            {lgrey}#######{reset}     {reset}{yellow}aaaa{reset}{orange}ggg{reset}{black}  {reset}
        {lgrey}###{reset}{orange}|¯|{reset}{lgrey}########{reset}{black}  {reset}{yellow}aaaa{reset}{magenta}ggg{reset}{black}  {reset}
        {black}  {reset}{lgrey}###{reset}{orange}|_|{reset}{lgrey}###{reset}{orange}|¯|{reset}{lgrey}#####{reset}{black}  {reset} {yellow}aa{reset}{magenta}gggg{reset}{black}  {reset}
    {black}  {reset}{blue}~~{reset}{lgrey}#########{reset}{orange}|_|{reset}{lgrey}########{reset}{black}  {reset}{black}  {reset}{magenta}ggg{reset}{black}  {reset}
    {black}  {reset}{blue}~~{reset}{black}  {reset}{lgrey}#################{reset}{blue}~~~~~{reset}{black}  {reset}
    {black}  {reset}{blue}~~~~~~{reset}{lgrey}#########{reset}{blue}~~~~~~~~{reset}{black}  {reset}{blue}~{reset}{black}  {reset}
    {black}  {reset}{black}  {reset}{blue}~~~~~~~~~~~~{reset}{black}      {reset}{blue}~~~~~{reset}{black}  {reset}
    {black} {reset}{yellow}$xxx{reset}{black}  {reset}{blue}~~~~~~{reset}{black}  {reset}{black}  {reset}{blue}~~~~~~~~~~~~{reset}{black}  {reset}
    {black} {reset}{yellow}$xxx{reset}{black}  {reset}{blue}~~~~{reset}{black}      {reset}{blue}~~~~~~~~~~~~{reset}{black}  {reset}
    {black}    {reset}{blue}~~~~~{reset}{black} {reset}{yellow}$xxx{reset}{black}  {reset}{blue}~~~~~~~~~~~~{reset}{black}  {reset}
    {black}  {reset}{blue}~~{reset}{black}  {reset}{blue}~~~{reset}{black} {reset}{yellow}$xxx{reset}{black}  {reset}{blue}~~~~~~~~~~~~{reset}{black}  {reset}
    {black}  {reset}{blue}~~{reset}{black}  {reset}{blue}~~~~{reset}{black}      {reset}{blue}~~~~~~~~~~{reset}{black}  {reset}
    {black}  {reset}{blue}~~~{reset}{black}  {reset}{blue}~~~~~~~~~{reset}{black}  {reset}{blue}~~~~~~~~{reset}{black}  {reset}
    {black}  {reset}{blue}~~~~{reset}{black}  {reset} {blue}~~~~~~~{reset}{black}  {reset}{blue}~~~~~~~~{reset}{black}  {reset}
    {black}  {reset}{blue}~~~~~~~{reset}{black}  {reset}{black}    {reset}{blue}~~~~{reset}{black}  {reset}{blue}~~~~{reset}{black}  {reset}{blue}~~{reset}{black}  {reset}
{black}  {reset}{blue}~~~~~~~~~~~~~~~~~~~~{reset}{black}  {reset}  {blue}~~~~~~{reset}{black}  {reset}
    {black}                     {reset}    {black}       {reset}
{green}~        ARE YOU A WIZARD?        ~{reset}
    """.format(
        black=bg('black'),
        yellow=bg('yellow'),
        orange=bg('orange_4b'),
        blue=fg('blue'),
        green=fg('green'),
        lgrey=fg('light_gray'),
        magenta=fg('magenta'),
        reset=attr('reset'))
    return wizard

def getTerminalWizard():
    wizard = None
    with open('timg_wizard.txt', 'r') as f:
        wizard = f.read()
    return wizard

def wipspell(event, context):
    response = getAsciiWizard()
    return response

def spell(event, context):
    response = getTerminalWizard()
    return response
