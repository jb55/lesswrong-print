import os
import glob
import sys

ROOT_DIR = "out/"

def main():
  html_dir = ROOT_DIR + sys.argv[1] + "/"
  md_dir = html_dir + "md/"
  html_files = glob.glob(html_dir + "*.html")

  for html_file in html_files:
    infile = html_file
    outfile = html_file.replace(".html", ".md");
    cmd = "pandoc %s -o %s" % (infile, outfile)
    os.system(cmd)

if __name__ == "__main__":
  main()
