from cx_Freeze import setup, Executable

setup(name='Youtube_to_text',
      version='1.0',
      description='Dada una url de youtube devuelve la transcripción en texto y en el portapapeles',
      executables=[Executable('youtube_to_text.py')],
      options={
          'build_exe': {
              'packages': ['os', 'youtube_transcript_api', 'sys', 'pyperclip'],
              'include_files': []
          }
      }
      )

