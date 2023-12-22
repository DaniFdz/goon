let
	pkgs = import <nixpkgs> {};
in 
	pkgs.mkShell {
		packages = [
			(pkgs.python311.withPackages (ps: with ps; [
				pip
				django
				coverage
				flake8
				pillow

				just
			]))
		];
	shellHook = ''
			# Tells pip to put packages into $PIP_PREFIX instead of the usual locations.
			# See https://pip.pypa.io/en/stable/user_guide/#environment-variables.
			export PIP_PREFIX=$(pwd)/_build/pip_packages
			export PYTHONPATH="$PIP_PREFIX/${pkgs.python311.sitePackages}:$PYTHONPATH"
			export PATH="$PIP_PREFIX/bin:$PATH"
			unset SOURCE_DATE_EPOCH
		'';
	}
